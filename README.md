# Emotion and Theme Recognition in Music Using Jamendo

The goal of this task is to automatically recognize the emotions and themes conveyed in a music recording using machine learning algorithms.

## Announcements
* **12 June: Data is now available to download**. We will announce the submission format and provide scripts to validate submissions soon.


## Task Schedule

* June-September: Participants work on algorithms
* September: Submissions open
* 20 September: Deadline for final submissions to organisers
* 25 September: Results returned to participants
* 1 October: Working notes deadline 
* 7 October: Feedback on working notes to participants 
* 11 October: Camera Ready version of working notes due
* October 27-29: MediaEval 2019 Workshop held near Nice, France

## Task Description

Emotion and theme recognition is a popular task in music information retrieval that is relevant for music search and recommendation systems. We invite the participants to try their skills at recognizing moods and themes conveyed by the audio tracks.

This task involves the prediction of moods and themes conveyed by a music track, given the raw audio. The examples of moods and themes are: happy, dark, epic, melodic, love, film, space etc. Each track is tagged with at least one tag that serves as a ground-truth.

Participants are expected to train a model that takes raw audio as an input and outputs the predicted tags. To solve the task, participants can use any audio input representation they desire, be it traditional handcrafted audio features or spectrograms or raw audio inputs for deep learning approaches. We will provide a handcrafted feature set extracted by the [Essentia](https://essentia.upf.edu/documentation/) audio analysis library as a reference. We allow usage of third-party datsets for model development and training, but it needs to be mentioned explicitly.

The generated outputs for the test dataset will be evaluated according to typical performance metrics like ROC-AUC, PR-AUC and micro/macro-averaged precision, recall and F-score.

We provide a dataset that is split into training, validation and testing subsets with emotion and theme labels properly balanced between subsets.

## Target Audience

Researchers in areas of music information retrieval, music psychology, machine learning a generally music and technology enthusiasts.


## Data

The dataset used for this task is the `autotagging-moodtheme` subset of the [MTG-Jamendo dataset](https://github.com/MTG/jamendo-dataset) [1], built using audio data from [Jamendo](https://jamendo.com) and made available under Creative Commons licenses. This subset includes 18,486 audio tracks with mood and theme annotations. In total, there are 57 tags, and tracks can possibly have more than one tag.

### Audio

We provide audio files in 320kbps MP3 format (152 GB) as well as NPY numpy archives with pre-computed mel-spectrograms (68 GB). To download the data use the [scripts and instructions provided for the MTG-Jamendo dataset](https://github.com/MTG/jamendo-dataset#downloading-the-dataset).

To download audio for the task, unpack and validate all tar archives:

```
mkdir /path/to/download
python3 scripts/download/download_gdrive.py --dataset autotagging_moodtheme --type audio /path/to/download --unpack --remove
```


Similarly, to download mel-spectrograms:
```
mkdir /path/to/download_melspecs
python3 scripts/download/download_gdrive.py --dataset autotagging_moodtheme --type melspecs /path/to/download --unpack --remove
```

### Training, validation and test data
The MTG-Jamendo dataset provides multiple random data splits for training, validation and testing (60-20-20%). For this challenge we use one of those splits ([split-0](https://github.com/MTG/jamendo-dataset/blob/master/data/splits/split-0)).

Participants should develop their systems using the provided [training](https://github.com/MTG/jamendo-dataset/blob/master/data/splits/split-0/autotagging_moodtheme-train.tsv) and [validation](https://github.com/MTG/jamendo-dataset/blob/master/data/splits/split-0/autotagging_moodtheme-validation.tsv) splits.

We place no restrictions on the use of 3rd party datasets for the development of the systems. In this case, we ask the participants to also provide a baseline system using only data from the official training/validation set.


## Submissions and evaluation
Participants should generate predictions for the [test split](https://github.com/MTG/jamendo-dataset/blob/master/data/splits/split-0/autotagging_moodtheme-test.tsv) and submit those to the task organizers.

To have a better understanding of the behavior of the proposed systems, we ask to submit both prediction (probability) scores and binary classification decisions for each tag for the tracks in the test set.

We will use the following metrics, both types commonly used in the evaluation of auto-tagging systems:
- **ROC-AUC** and **PR-AUC** on tag prediction scores
- Micro- and macro-averaged **precision**, **recall** and **F-score** for binary predictions.

Participants should report the obtained metric scores on the validation split and test split if they have run such a test on their own. Participants should also report whether they used the whole development dataset or only its part for every submission.

We allow only five evaluation runs per participating team.

Note that we rely on the fairness of submissions and do not hide the ground truth for the test split. It is publicly available for benchmarking as a part of the MTG-Jamendo dataset outside this challenge. For transparency and reproducibility, we encourage the participants to publically release their code under an open-source/free software license.


## Baseline approach
A baseline approach will be announced soon.


## Recommended reading

[1] Bogdanov, D., Won M., Tovstogan P., Porter A., & Serra X. (2019).  [The MTG-Jamendo Dataset for Automatic Music Tagging](http://mtg.upf.edu/node/3957). Machine Learning for Music Discovery Workshop, International Conference on Machine Learning (ICML 2019).

[2] Soleymani, M., Caro, M. N., Schmidt, E. M., Sha, C. Y., & Yang, Y. H. (2013). [1000 songs for emotional analysis of music](https://ibug.doc.ic.ac.uk/media/uploads/documents/cmm13-soleymani.pdf). In Proceedings of the 2nd ACM international workshop on Crowdsourcing for multimedia (CrowdMM 2013), (pp. 1-6).

[3] Aljanaki, A., Yang, Y. H., & Soleymani, M. (2014, October). [Emotion in Music Task at MediaEval 2014](http://ceur-ws.org/Vol-1263/mediaeval2014_submission_33.pdf).

[4] Panda, R., Malheiro, R., & Paiva R. P. (2018). [Musical Texture and Expressivity Features for Music Emotion Recognition](http://mir.dei.uc.pt/pdf/Conferences/MOODetector/ISMIR_2018_Panda.pdf). In Proceedings of the International Society on Music Information Retrieval Conference (ISMIR2018), (pp. 383-391).

[5] Laurier, C., Meyers, O., Serra, J., Blech, M., & Herrera, P. (2009). [Music mood annotator design and integration](http://mtg.upf.edu/files/publications/Laurier_MusicMoodAnnotator.pdf). In 7th International Workshop on Content-Based Multimedia Indexing (CBMI'09), (pp. 156-161).

[6] Kim, Y. E., Schmidt, E. M., Migneco, R., Morton, B. G., Richardson, P., Scott, J., Speck, J. A. & Turnbull, D. (2010, August). [Music emotion recognition: A state of the art review](http://ismir2010.ismir.net/proceedings/ismir2010-45.pdf). In Proceedings of the International Society on Music Information Retrieval Conference (ISMIR2010), (pp. 255-266).

[7] Hu, X., & Downie, J. S. (2007). [Exploring Mood Metadata: Relationships with Genre, Artist and Usage Metadata](http://ismir2007.ismir.net/proceedings/ISMIR2007_p067_hu.pdf). In Proceedings of the International Conference on Music Information Retrieval (ISMIR2007), pp. 67-72.

## Task organizers

Music Technology Group, Universitat Pompeu Fabra, Spain (first.last@upf.edu):

- Dmitry Bogdanov
- Alastair Porter
- Philip Tovstogan
- Minz Won

## Acknowledgements

[MIP-Frontiers](https://mip-frontiers.eu/), [Jamendo](https://www.jamendo.com/)

<img src="img/mip-frontiers.png" height="64" hspace="20"><img src="img/jamendo-licensing.svg" height="64" hspace="20">

This project has received funding from the European Union's Horizon 2020 research and innovation programme under the Marie Skłodowsa-Curie grant agreement No. 765068

<img src="img/eu.svg" height="64" hspace="20">
