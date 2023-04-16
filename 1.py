from transformers import BertModel

# 加载BERT模型
bert_model = BertModel.from_pretrained('bert-base-uncased')

# 查看模型名称
print(bert_model.__class__.__name__)
