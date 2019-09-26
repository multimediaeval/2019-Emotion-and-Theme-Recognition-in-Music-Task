# Emotion and Theme Recognition in Music Using Jamendo

The goal of this task is to automatically recognize the emotions and themes conveyed in a music recording using machine learning algorithms.

## Announcements
* **25 September: The [results](./results) are out!**
* 3 September: Final baseline results are now available.
* 27 August: We have added more details about the use of the validation set and evaluation.
* 7 August: We have formalized the submission format and now provide evaluation scripts for self-evaluation, see *submissions and evaluations* section below
* 1 August: We have expanded our dataset with pre-computed statistical features from [Essentia](https://essentia.upf.edu) using the feature extractor for [AcousticBrainz](https://acousticbrainz.org/). These features are were previously used in the MediaEval genre recognition tasks in [2017](https://multimediaeval.github.io/2017-AcousticBrainz-Genre-Task/) and [2018](https://multimediaeval.github.io/2018-AcousticBrainz-Genre-Task/).
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

Participants are expected to train a model that takes raw audio as an input and outputs the predicted tags. To solve the task, participants can use any audio input representation they desire, be it traditional handcrafted audio features or spectrograms or raw audio inputs for deep learning approaches. We also provide a handcrafted feature set extracted by the [Essentia](https://essentia.upf.edu/documentation/) audio analysis library as a reference. We allow usage of third-party datsets for model development and training, but it needs to be mentioned explicitly.

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
python3 scripts/download/download.py --dataset autotagging_moodtheme --type audio /path/to/download --unpack --remove
```


Similarly, to download mel-spectrograms:
```
mkdir /path/to/download_melspecs
python3 scripts/download/download.py --dataset autotagging_moodtheme --type melspecs /path/to/download_melspecs --unpack --remove
```

To download Essentia (AcousticBrainz) features:
```
mkdir /path/to/download_acousticbrainz
python3 scripts/download/download.py --dataset autotagging_moodtheme --type acousticbrainz /path/to/download_acousticbrainz --unpack --remove
```


### Training, validation and test data
The MTG-Jamendo dataset provides multiple random data splits for training, validation and testing (60-20-20%). For this challenge we use one of those splits ([split-0](https://github.com/MTG/jamendo-dataset/blob/master/data/splits/split-0)).

Participants should develop their systems using the provided [training](https://github.com/MTG/jamendo-dataset/blob/master/data/splits/split-0/autotagging_moodtheme-train.tsv) and [validation](https://github.com/MTG/jamendo-dataset/blob/master/data/splits/split-0/autotagging_moodtheme-validation.tsv) splits.

The validation set should be used for tuning hyperparameters of the models and regularization against overfitting by early stopping. These optimizations should not be done using the test set, which should be only used to estimate the performance of the final submissions.

We place no restrictions on the use of 3rd party datasets for the development of the systems. In this case, we ask the participants to also provide a baseline system using only data from the official training/validation set. Similarly, if one wants to append validation set to the training data to build a model using more data for the final submission, a baseline using only training set for training should be provided.

## Submissions and evaluation
Participants should generate predictions for the [test split](https://github.com/MTG/jamendo-dataset/blob/master/data/splits/split-0/autotagging_moodtheme-test.tsv) and submit those to the task organizers.

To have a better understanding of the behavior of the proposed systems, we ask to submit both **prediction** (probability) scores and binary classification **decisions** for each tag for the tracks in the test set. We provide a [script](https://github.com/MTG/mtg-jamendo-dataset/blob/master/scripts/mediaeval2019/calculate_decisions.py) to calculate activation thresholds and generate decisions from predictions by maximizing macro F-score.

The submission format is two `.npy` files containing a numpy matrix with rows representing tracks and columns - tags. The dimensions should be **4231 tracks x 56 tags**. The order of tracks should be the same as in the test split and the order of tags is an alphabetically sorted one, please refer to [this file](https://github.com/MTG/mtg-jamendo-dataset/blob/master/data/tags/moodtheme_split.txt). Use `numpy.save()` to create submission files:
- `decisions.npy`: `dtype('bool')`, `shape=(4231, 56)`
- `predictions.npy`: `dtype('float64')`, `shape=(4231, 56)`

We will use the following metrics, both types commonly used in the evaluation of auto-tagging systems:
- Macro **ROC-AUC** and **PR-AUC** on tag prediction scores
- Micro- and macro-averaged **precision**, **recall** and **F-score** for binary predictions.

Participants should report the obtained metric scores on the validation split and test split if they have run such a test on their own. Participants should also report whether they used the whole development dataset or only its part for every submission. We provide the scripts to do that in [mtg-jamendo-dataset repository](https://github.com/MTG/mtg-jamendo-dataset/blob/master/scripts/mediaeval2019):

```
cd /path/to/mtg-jamendo-dataset/scripts
python3 mediaeval2019/evaluate.py ../data/mediaeval2019/groundtruth.npy ../data/mediaeval2019/predictions.npy ../results/mediaeval2019/decisions.npy --output-file ../results/mediaeval2019/results.tsv
```

To generate decisions from predictions using provided script:
```
python3 mediaeval2019/calculate_decisions.py ../results/mediaeval2019/groundtruth.npy ../results/mediaeval2019/my_predictions.npy ../data/mediaeval2019/my_thresholds.txt ../data/tags/moodtheme_split.txt --decision-file ../data/mediaeval2019/my_decisions.npy
```

We will generate rankings of the submissions by ROC-AUC, PR-AUC and micro and macro F-score. For the leaderboard purposes we will use **PR-AUC** as the main metric, however we encourage comprehensive evaluation of the systems by using all metrics with the goal of generating more valuable insights on the proposed models when reporting evaluation results in the working notes.

We allow only five evaluation runs per participating team.

Note that we rely on the fairness of submissions and do not hide the ground truth for the test split. It is publicly available for benchmarking as a part of the MTG-Jamendo dataset outside this challenge. For transparency and reproducibility, we encourage the participants to publically release their code under an open-source/free software license.


## Baselines
### VGG-ish baseline approach
We used a broadly used [vgg-ish architecture](https://arxiv.org/pdf/1606.00298.pdf) as our baseline. It consists of five 2D convolutional layers followed by a dense connection. Reproducible codes are available in [mtg-jamendo-dataset repository](https://github.com/MTG/mtg-jamendo-dataset/tree/master/scripts/baseline). We trained our model for 1000 epochs and used the validation set to choose the best model. Then we have found optimizal decision thresholds for the activation values individually for each tag, maximizing macro F-score ([script](https://github.com/MTG/mtg-jamendo-dataset/blob/master/scripts/mediaeval2019/calculate_decisions.py)). 

Our experimental result was:
```
ROC-AUC            0.725821
PR-AUC             0.107734
precision-macro    0.138216
recall-macro       0.308650
F-score-macro      0.165694
precision-micro    0.116097
recall-micro       0.373480
F-score-micro      0.177133
```

and tag-wise AUCs were:

```
mood/theme---action			0.6590 , 0.0312
mood/theme---adventure			0.6250 , 0.0803
mood/theme---advertising		0.7798 , 0.2477
mood/theme---background			0.7059 , 0.0376
mood/theme---ballad			0.7109 , 0.0542
mood/theme---calm			0.6805 , 0.0361
mood/theme---children			0.7396 , 0.1244
mood/theme---christmas			0.7114 , 0.1069
mood/theme---commercial			0.6707 , 0.0654
mood/theme---cool			0.7204 , 0.0215
mood/theme---corporate			0.8721 , 0.3373
mood/theme---dark			0.7409 , 0.2183
mood/theme---deep			0.9347 , 0.5761
mood/theme---documentary		0.6485 , 0.0592
mood/theme---drama			0.5952 , 0.0253
mood/theme---dramatic			0.6786 , 0.0378
mood/theme---dream			0.5843 , 0.0815
mood/theme---emotional			0.6190 , 0.1327
mood/theme---energetic			0.7118 , 0.1186
mood/theme---epic			0.8197 , 0.3080
mood/theme---fast			0.8242 , 0.0266
mood/theme---film			0.7595 , 0.3441
mood/theme---fun 			0.8264 , 0.0773
mood/theme---funny			0.6681 , 0.0279
mood/theme---game			0.6971 , 0.0480
mood/theme---groovy			0.7609 , 0.0238
mood/theme---happy			0.7618 , 0.2534
mood/theme---heavy			0.9067 , 0.1260
mood/theme---holiday			0.6415 , 0.0153
mood/theme---hopeful			0.6336 , 0.0323
mood/theme---inspiring			0.6450 , 0.0916
mood/theme---love			0.7276 , 0.1205
mood/theme---meditative			0.8070 , 0.1669
mood/theme---melancholic		0.6606 , 0.0475
mood/theme---melodic			0.6676 , 0.0977
mood/theme---motivational		0.7945 , 0.2012
mood/theme---movie			0.5419 , 0.0250
mood/theme---nature			0.6315 , 0.0458
mood/theme---party			0.8026 , 0.0420
mood/theme---positive			0.7676 , 0.0901
mood/theme---powerful			0.8004 , 0.1119
mood/theme---relaxing			0.6814 , 0.1233
mood/theme---retro			0.7897 , 0.0247
mood/theme---romantic			0.7098 , 0.0735
mood/theme---sad 			0.6895 , 0.1050
mood/theme---sexy			0.7432 , 0.0238
mood/theme---slow			0.6490 , 0.0399
mood/theme---soft			0.7250 , 0.0681
mood/theme---soundscape			0.7971 , 0.0432
mood/theme---space			0.7704 , 0.0572
mood/theme---sport			0.8375 , 0.0571
mood/theme---summer			0.8914 , 0.4466
mood/theme---trailer			0.8536 , 0.1519
mood/theme---travel			0.5629 , 0.0097
mood/theme---upbeat			0.7059 , 0.0398
mood/theme---uplifting			0.7052 , 0.0540
```
### Popularity baseline
Popularity baseline always predicts the most frequent tag among tracks in the training set:
```
ROC-AUC            0.500000
PR-AUC             0.031924
precision-macro    0.001427
recall-macro       0.017857
F-score-macro      0.002642
precision-micro    0.079887
recall-micro       0.044685
F-score-micro      0.057312
```

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
