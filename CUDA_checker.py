import torch


def main():
    print("GPU available with CUDA:", torch.cuda.is_available())
    if not torch.cuda.is_available():
        return
    print("Index of current CUDA GPU device:", torch.cuda.current_device())
    print("Number of available GPUs with CUDA:", torch.cuda.device_count())
    for gpu in range(torch.cuda.device_count()):
        print()
        print("GPU #" + str(gpu))
        print("Device:", torch.cuda.device(gpu))
        print("Name:", torch.cuda.get_device_name(gpu))


if __name__ == '__main__':
    main()
