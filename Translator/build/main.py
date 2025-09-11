import tkinter as tk
from gui import create_gui
from seq2seq_model import Seq2SeqModel

def main():
    # Create a Tkinter window
    window = tk.Tk()

    # Define the vocabulary sizes for source and target languages
    source_vocab_size = 100
    target_vocab_size = 100

    # Define the model parameters
    FLAGS = {
        "learning_rate": 0.5,
        "learning_rate_decay_factor": 0.99,
        "max_gradient_norm": 5.0,
        "batch_size": 32,
        "size": 512,
        "num_layers": 2,
        "s_vocab_size": source_vocab_size,
        "t_vocab_size": target_vocab_size,
        "data_dir": "/Users/fancyshmancy/Development/nlp/proj2/data/",
        "train_dir": "/Users/fancyshmancy/Development/nlp/proj2/runs/de_en_lstm_reg/",
        "max_train_data_size": 0,
        "steps_per_checkpoint": 200,
        "use_fp16": False
    }

    # Initialize the model
    model = Seq2SeqModel(FLAGS)

    # Call the function to create the GUI within the window
    create_gui(window, model)

if __name__ == "__main__":
    main()






