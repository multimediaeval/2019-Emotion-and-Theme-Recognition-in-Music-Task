# 2019-Emotion-and-Theme-Recognition-in-Music-Using-Jamendo
The goal of this task is to recognize the emotions and themes conveyed in a music recording.

## Task Description

Emotion and theme recognition is a popular task in music information retrieval that is relevant for music search and recommendation systems. We invite the participants to try their skills at recognizing moods and themes conveyed by the audio tracks.

This task involves the prediction of moods and themes conveyed by a music track, given the raw audio. The examples of moods and themes are: happy, dark, epic, melodic, love, film, space etc. Each track is tagged with at least one tag that serves as a ground-truth.

Participants are expected to train a model that takes raw audio as an input and outputs the predicted tags. To solve the task, participants can use any audio input representation they desire, be it traditional handcrafted audio features or spectrograms or raw audio inputs for deep learning approaches. We will provide a handcrafted feature set extracted by the [Essentia](https://essentia.upf.edu/documentation/) audio analysis library as a reference.

The generated outputs for the test dataset will be evaluated according to typical accuracy metrics like ROC-AUC and PR-AUC.

We provide a dataset that is split into training, validation and testing subsets with emotion and theme labels properly balanced.

Emotion recognition can have various applications such as in auto-tagging or recommendation systems. What differentiates this task from a generic auto-tagging problem is that we want to identify features (either engineered or learned by deep learning architectures) that are good at distinguishing tags in terms of arousal-valence representation of human emotion [2].

## Target group

Researchers in areas of music information retrieval, music psychology, machine learning a generally music and technology enthusiasts.

## Data

Raw audio data is provided by Jamendo under Creative Commons license and includes 50k audio tracks with mood and theme annotations. There are 267 tags with tracks possibly having more than one tag. 204 of those tags have arousal and valence values.

## Evaluation methodology

For this task we are using 2 metrics: **ROC-AUC** and **PR-AUC** for measuring the accuracy of tags (agnostic to the meaning of tags)

## Recommended reading

[1] Soleymani, M., Caro, M. N., Schmidt, E. M., Sha, C. Y., & Yang, Y. H. (2013). 1000 songs for emotional analysis of music. In Proceedings of the 2nd ACM international workshop on Crowdsourcing for multimedia (CrowdMM 2013), (pp. 1-6).

[2]Aljanaki, A., Yang, Y. H., & Soleymani, M. (2014, October). Emotion in Music Task at MediaEval 2014. In MediaEval.

[3] Panda, R., Malheiro, R., & Paiva R. P. (2018). Musical Texture and Expressivity Features for Music Emotion Recognition. In Proceedings of the International Society on Music Information Retrieval Conference (ISMIR2018), (pp. 383-391).

[4] Laurier, C., Meyers, O., Serra, J., Blech, M., & Herrera, P. (2009). Music mood annotator design and integration. In 7th International Workshop on Content-Based Multimedia Indexing (CBMI'09), (pp. 156-161).

[5] Kim, Y. E., Schmidt, E. M., Migneco, R., Morton, B. G., Richardson, P., Scott, J., ... & Turnbull, D. (2010, August). Music emotion recognition: A state of the art review. In Proceedings of the International Society on Music Information Retrieval Conference (ISMIR2010), (pp. 255-266).

[6] Hu, X., & Downie, J. S. (2007). Exploring Mood Metadata: Relationships with Genre, Artist and Usage Metadata. In Proceedings of the International Conference on Music Information Retrieval (ISMIR2007), pp. 67-72.

## Task organizers

Music Technology Group, Universitat Pompeu Fabra, Spain (first.last@upf.edu):

- Dmitry Bogdanov
- Alastair Porter
- Philip Tovstogan

## Acknowledgements

[MIP-Frontiers](https://mip-frontiers.eu/), [Jamendo](https://www.jamendo.com/)

<img src="img/mip.svg" height="64" hspace="20"><img src="img/jamendo-licensing.svg" height="64" hspace="20">

This project has received funding from the European Union's Horizon 2020 research and innovation programme under the Marie Skłodowsa-Curie grant agreement No. 765068

<img src="img/eu.svg" height="64" hspace="20">
