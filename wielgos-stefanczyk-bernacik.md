# Przetwarzanie w chmurze - self-hosted Ray cluster (Kubernetes)

## Cel projektu

Celem projektu będzie wdrożenie klastra Ray z użyciem operatora Kubernetes'owego (KubeRay) self-hosted na własnych node'ach (utworzonych z komputerów lokalnych, VM, VPS, RaspberryPi) i poprowadzenie na nim CPU-intensive obliczeń: takich jak fine-tuning modelu, inferencja modelu, trenowanie modelu.

## Skład zespołu

- Kamil Bernacik
- Artur Stefańczyk
- Mikołaj Wielgos

## Motywacja

Motywacją dla nas przede wszystkim była możliwość uruchomienia klastra Ray na własnych node'ach na własnych VM/VPS. Moc obliczeniowa, którą w ten sposób moglibyśmy pozyskać do wszelakich zadań (raczej CPU-only) byłaby znacznie tańsza aniżeli korzystanie z Managed Ray Service, czy chociażby EKS/GKS.

## Related Work

W literaturze oraz dokumentacji technicznej istnieje wiele podejść do uruchamiania klastrów obliczeniowych w modelu self-hosted. Poniższe prace i projekty są szczególnie istotne dla naszego podejścia:
- **Ray on Kubernetes** – dokumentacja oficjalna Ray przedstawia sposoby wdrażania klastra na Kubernetesie, w tym integrację z autoskalowaniem i dynamiczną alokacją zasobów.
- **KubeRay** – projekt rozwijany przez społeczność, który upraszcza zarządzanie klastrami Ray na Kubernetesie, zapewniając lepszą integrację z ekosystemem cloud-native.
- **Dask Kubernetes** – podobny koncept do Ray, wykorzystywany głównie w analizie danych i obliczeniach rozproszonych, oferujący porównywalne mechanizmy skalowania.
- **Apache Spark on Kubernetes** – spark od dawna wspiera Kubernetes, co może służyć jako punkt odniesienia dla projektowania klastrów Ray w podobnym środowisku.

## Literatura

- Moritz, P., Nishihara, R., Wang, S., Tumanov, A., Liaw, R., Liang, E., ... & Stoica, I. (2018). **Ray: A Distributed Framework for Emerging AI Applications**. OSDI 2018.
- Bernstein, D. (2014). **Containers and Cloud: From LXC to Docker to Kubernetes**. IEEE Cloud Computing.
- Verma, A., Pedrosa, L., Korupolu, M., Oppenheimer, D., Tune, E., & Wilkes, J. (2015). **Large-Scale Cluster Management at Google with Borg**. EuroSys.