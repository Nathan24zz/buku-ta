from openvino.runtime import Core

# Load the network in OpenVINO Runtime.
ie = Core()
model_ir = ie.read_model(model='/path/to/model-name.xml')
compiled_model_ir = ie.compile_model(model=model_ir, device_name="CPU")
