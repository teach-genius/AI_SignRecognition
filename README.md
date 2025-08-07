# SilentVoice
SilentVoice is an interactive learning platform for `American Sign Language (ASL)`.

The user performs signs in front of their camera, our recognition system analyzes the movement in real-time, and a voice assistant instantly confirms whether the sign matches the targeted letter. 
This interactive approach transforms traditional ASL learning into a personalized and autonomous experience.

## Dataset
For this project, we used the [ASL Alphabet](https://www.kaggle.com/datasets/debashishsau/aslamerican-sign-language-aplhabet-dataset)  dataset, which is a collection of images representing the American Sign Language (ASL) alphabet. The total dataset size is **4.56 GB**.

The original dataset contains RGB color images of different letters of the ASL alphabet. For our study, we used only the `asl_alphabet_train` folder, which contains approximately **8000 images per class** for the **26 letters** of the alphabet (A-Z) plus the `NOTHING` class.

### Data Organization

| Characteristic | Description |
|----------|----------|
| Total Classes  |27 (A-Z + NOTHING)  |
| Images per Class | ~8000 (variable per class)|
|Image Format | RGB Color Images|
|File Size| Between 160 KB and 270 KB per image|
|Total Dataset Size| 4.56 GB |

## Data Preprocessing
We divided the `asl_alphabet_train` dataset into the following split:

- 70% for training (Train)

- 15% for validation (Val)

- 15% for testing (Test)
  
To enhance our dataset and improve model robustness, we implemented multiple **data augmentation techniques** using Keras `ImageDataGenerator`. The applied transformations include:

|Transformation | Description | 
|---------------|--------------|
|Normalization | sample-wise normalization|
|Rotation| Random rotation up to 30 degree| 
| Shear | Shear transformation with factor 0.2| 
| Zoom | Random zoom with factor 0.2| 
|Translation| Horizontal and vertical shift up to 20%|
|Brightness | Brightness variation of ±20%|

## Model Architecture
Our solution is based on a **Convolutional Neural Network (CNN)** composed of **five convolutional blocks** followed by fully connected layers. The architecture is structured as follows:

### Layer Structure

- **Input Layer**

    - Dimension: **64×64×1** (grayscale images)

- **Convolutional Blocks**

    - **Block 1:** Conv2D(32) → MaxPooling → BatchNormalization

    - **Block 2:** Conv2D(64) → MaxPooling → BatchNormalization

    - **Block 3:** Conv2D(128) → MaxPooling → BatchNormalization

    - **Block 4:** Conv2D(256) → MaxPooling → BatchNormalization

    - **Block 5:** Conv2D(512) → MaxPooling → BatchNormalization

- **Classification Layers**

    - Dense(256) with ReLU and Dropout(0.5)

    - Dense(128) with ReLU and Dropout(0.5)

    - Dense(27) with Softmax

## Model Performance

The model achieved the following performance on the test set :
| Metric    | Value  |
| --------- | ------ |
| Accuracy  | 0.9642 |
| Loss      | 0.1157 |
| F1 Score  | 0.9364 |
| Precision | 0.9373 |
| Recall    | 0.9363 |

## User Interface
### Connection Page
The first page requires the user to enter their email to gain access to the application

<p align="center">
  <img src="https://github.com/user-attachments/assets/b076d5ca-9b83-43e0-838d-6668bdf6aa32" />
</p>

### Functionality Overview Page
Once logged in, users are directed to a page that outlines the main functionalities of **SilentVoice**, explaining how the system works.

<p align="center">
  <img src="https://github.com/user-attachments/assets/a74dcb90-a235-4236-b2b7-2bff79ef1086" />
</p>

### Main Interaction Interface
The core application interface where users can:
- Perform ASL signs in front of their camera.
- A gesture recognition model that analyzes movements in real-time.
- Get instant audio confirmation if the sign is correct.
- A reference sheet displayed, showing the complete ASL alphabet, allowing immediate correction of incorrect movements.

<p align="center">
  <img src="https://github.com/user-attachments/assets/e0215d7c-f387-43b9-adda-c733faf02782" />
</p>

## Run Locally

Clone the project

```bash
  git clone https://github.com/hibaaaaaaaaaaa/SilentVoice.git
```

Go to the project directory

```bash
  cd SilentVoice
```

Install dependencies

```bash
  pip install -r requirements.txt
```

Start the application:

```bash
  python main.py
```

## Authors

- [@hibasofyan](https://github.com/hibaaaaaaaaaaa)
- [@chantryolandaeyiba](https://github.com/aryadacademie)



