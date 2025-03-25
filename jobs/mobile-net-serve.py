import io
from typing import Dict, List

import ray
import tensorflow as tf
import numpy as np
from PIL import Image
from starlette.requests import Request
from ray import serve

@serve.deployment
class MobileNetDeployment:
    def __init__(self):
        """
        Initialize the MobileNet model with ImageNet weights.
        Preload model to avoid repeated loading for each request.
        """
        self.model = tf.keras.applications.MobileNetV2(weights='imagenet')
        self.preprocess_input = tf.keras.applications.mobilenet_v2.preprocess_input
        self.decode_predictions = tf.keras.applications.mobilenet_v2.decode_predictions

    async def __call__(self, request: Request) -> Dict:
        """
        Handle image classification requests.
        Expects multipart/form-data with an image file.
        """
        # Read image from request
        form = await request.form()
        image_file = form['image']
        image_bytes = await image_file.read()

        # Process and classify image
        image = Image.open(io.BytesIO(image_bytes)).resize((224, 224))
        image_array = np.array(image)
        image_array = np.expand_dims(image_array, axis=0)
        image_array = self.preprocess_input(image_array)
        
        # Predict and decode predictions
        preds = self.model.predict(image_array)
        results = self.decode_predictions(preds, top=3)[0]
        
        # Format results for JSON response
        formatted_results = [
            {
                "rank": i + 1, 
                "label": label, 
                "score": float(score)
            } 
            for i, (imagenet_id, label, score) in enumerate(results)
        ]
        
        return {"predictions": formatted_results}

# Create and bind the deployment
app = MobileNetDeployment.bind()

if __name__ == "__main__":
    # Start the Ray Serve instance locally
    serve.run(app)