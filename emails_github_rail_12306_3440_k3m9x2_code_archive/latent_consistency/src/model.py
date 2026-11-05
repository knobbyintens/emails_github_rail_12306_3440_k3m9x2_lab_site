"""Reference implementation skeleton for:

Latent Consistency Distillation for Streaming Speech Translation
"""

import torch


class Model(torch.nn.Module):
    def __init__(self, hidden_size: int = 512) -> None:
        super().__init__()
        self.hidden_size = hidden_size

    def forward(self, x):  # pragma: no cover - skeleton
        return x
