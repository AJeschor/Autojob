from transformers import BertModel
from adapters import AutoAdapterModel

# Constants for model, adapter, and output file name
MODEL_NAME = "bert-base-uncased"
ADAPTER_NAME = "PanoEvJ/GenAI-CoverLetter"
OUTPUT_FILE_NAME = "adapter_info.tsv"

def initialize_model_and_adapter():
    """
    Initialize the BERT model and load the specified adapter.

    Returns:
        BertModel: Initialized BERT model.
        AutoAdapterModel: Initialized adapter model.
    """
    bert_model = BertModel.from_pretrained(MODEL_NAME)
    adapter_model = AutoAdapterModel(bert_model)
    adapter_model.load_adapter(ADAPTER_NAME, set_active=True)
    return bert_model, adapter_model

def write_adapter_info_to_tsv(adapter_infos, file_name):
    """
    Write adapter information to a TSV file.

    Args:
        adapter_infos (list): List of AdapterInfo objects to write to the file.
        file_name (str): Name of the output TSV file.
    """
    with open(file_name, "w") as file:
        # Write header
        file.write("Source\tAdapter_ID\tModel_Name\tTask\tSubtask\tUsername\tAdapter_Config\tSHA1_Checksum\n")
        # Write data
        for adapter_info in adapter_infos:
            file.write(f"{adapter_info.source}\t{adapter_info.adapter_id}\t{adapter_info.model_name}\t{adapter_info.task}\t{adapter_info.subtask}\t{adapter_info.username}\t{adapter_info.adapter_config}\t{adapter_info.sha1_checksum}\n")

def main():
    # Initialize BERT model and adapter
    bert_model, adapter_model = initialize_model_and_adapter()
    # List available adapters
    adapter_infos = adapter_model.list_adapters()
    # Write adapter information to a TSV file
    write_adapter_info_to_tsv(adapter_infos, OUTPUT_FILE_NAME)

if __name__ == "__main__":
    main()
