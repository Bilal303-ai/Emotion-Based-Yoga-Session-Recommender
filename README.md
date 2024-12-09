# Emotion-Based-Yoga-Session-Recommender

This project utilizes a fine-tuned **DistilHuBERT** model to classify emotions from audio inputs and recommend tailored yoga sessions. The application was built using Hugging Face's Transformers library and Gradio for the user interface.

## Approach
1. **Dataset:** The **Ravdess** dataset, comprising 1,440 audio files with 8 emotion labels: calm, happy, sad, angry, fearful, surprise, neutral, and disgust (merged into other labels).
2. **Model Fine-Tuning:** The DistilHuBERT model was fine-tuned for 7 epochs with a learning rate of 5e-5, achieving an accuracy of 98% on the test dataset.
3. **Application:** Gradio was used to create a user-friendly interface, which takes an audio input, detects the emotion, and suggests a yoga session based on the detected mood.

## Data Preprocessing
- **Sampling Rate**: Audio files were resampled to 16kHz to match the model's requirements.
- **Padding:** Audio clips shorter than 30 seconds were zero-padded.
- **Train-Test Split:** 80% of the samples were used for training, and 20% for testing.

##  Model Architecture
- **DistilHuBERT:** A lightweight variant of HuBERT, fine-tuned for emotion classification.
- **Fine-Tuning Setup:**
    - Optimizer: AdamW
    - Loss Function: Cross-Entropy
    - Learning Rate: 5e-5
    - Warm-up Ratio: 0.1
    - Epochs: 7
 
## Results
- **Accuracy:** 0.98 on the test dataset
- **Loss:** 0.10 on the test dataset
- **Emotion Mapping:** Each emotion is linked to a predefined yoga session in the sessions.py file.

## Next Steps
- **Dataset Expansion:** Incorporate additional datasets for better generalization.
- **Real-Time Processing:** Optimize the model for real-time emotion detection.
- **Integration:** Deploy the application for wider usage.
- **Customization:** Allow users to input their preferences for yoga session recommendations.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/Bilal303-ai/Emotion-Based-Yoga-Session-Recommender
   cd Emotion-Based-Yoga-Session-Recommender
   ```
2. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the app:
   ```bash
   python app.py
   ```

## Demo
You can access the live demo of the app on [Hugging Face](https://huggingface.co/spaces/BilalHasan/Mood-Based-Yoga-Session-Recommendation).
    
