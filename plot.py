import matplotlib.pyplot as plt
import numpy as np
# Create range of values for parameter
param_range = np.arange(1, 11, 1)
# Calculate accuracy on training and test set using range of parameter values


# Plot accurancy bands for training and test sets
# plt.fill_between(param_range, train_mean - train_std, train_mean + train_std, color="gray")
# plt.fill_between(param_range, test_mean - test_std, test_mean + test_std, color="gainsboro")


def plot_training_acc():
    train_scores = [0.8046, 0.8469, 0.8571, 0.8705, 0.8847, 0.8819, 0.8927, 0.8974, 0.8978, 0.9091]
    plt.plot(param_range, train_scores, label="crfrnn", color="dimgrey")
    plt.title("Training Accuracy")
    plt.xlabel("epoch")
    plt.ylabel("accuracy")
    plt.tight_layout()
    plt.legend(loc="best")
    plt.savefig("train_accuracy.png")
    plt.show()


def plot_validation_acc():
    test_scores = [0.6430, 0.5184, 0.6200, 0.6569, 0.5945, 0.4024, 0.6596, 0.7298, 0.6680, 0.7689]
    plt.plot(param_range, test_scores, label="crfrnn", color="dimgrey")
    plt.title("Validation Accuracy")
    plt.xlabel("epoch")
    plt.ylabel("accuracy")
    plt.tight_layout()
    plt.legend(loc="best")
    plt.savefig("validation_accuracy.png")
    plt.show()


def main():
    plot_training_acc()
    plot_validation_acc()


if __name__ == '__main__':
    main()
