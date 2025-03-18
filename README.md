# DistilGPT2 Fine-Tuning for n8n Workflow Generation

This repository contains the fine-tuning process of DistilGPT-2 for generating efficient **n8n workflows** based on pre-processed JSON datasets. The model is trained on a dataset of 331 input-output entries, enabling it to generate structured workflows based on text prompts.

## 📌 Project Overview

The objective of this project is to fine-tune **DistilGPT-2** on a dataset containing structured JSON workflows. The model learns to generate n8n-compatible JSON outputs from textual descriptions, helping automate workflow generation.


## 🚀 Features

- Fine-tunes **DistilGPT-2** using a structured dataset of **n8n JSON workflows**.
- Generates **valid workflow JSONs** from text inputs.
- Optimized for **low-latency** inference.
- Implements **preprocessing, training, and validation pipelines**.

## 📊 Dataset

- The dataset consists of **331 input-output pairs** of text prompts and n8n workflow JSONs.
- Preprocessing includes tokenization and formatting for GPT-style training.

## 🔥 Model Training

- Model: **DistilGPT-2**
- Training Data: **Pre-processed n8n workflows**
- Framework: **Hugging Face Transformers**
- Training Method: **Supervised fine-tuning**
- Optimizations: **Gradient checkpointing, mixed precision training**

## 📈 Results & Evaluation

- The fine-tuned model successfully generates **structured n8n workflows**.
- Accuracy and performance are evaluated using **execution correctness**.

## 🤖 Future Improvements

- Enhance dataset with **more complex workflows**.
- Implement **RLHF (Reinforcement Learning with Human Feedback)** for better output quality.
- Integrate **n8n API for real-time validation**.

## 📜 License

This project is licensed under the MIT License.

---

🔗 **Contributions & Feedback**  
Feel free to open issues and contribute to the project!

---
