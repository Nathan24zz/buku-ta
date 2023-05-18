import torch

model = # Model definiton in PyTorch
model.eval()
dummy_input = # In this case an image loaded with OpenCV

torch.onnx.export(model, dummy_input, "model-name.onnx")