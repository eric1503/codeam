"""Loader konfigurasi dari config.yaml."""
import os
import yaml


class Config(dict):
    """Dict yang bisa diakses pakai atribut: cfg.strategy["ema_fast"]."""

    def __getattr__(self, name):
        try:
            val = self[name]
        except KeyError:
            raise AttributeError(name)
        return Config(val) if isinstance(val, dict) else val


def load_config(path: str = "config.yaml") -> Config:
    if not os.path.exists(path):
        raise FileNotFoundError(
            f"'{path}' tidak ditemukan. Copy config.example.yaml jadi config.yaml "
            "lalu isi token Telegram & login MT5 kamu."
        )
    with open(path, "r", encoding="utf-8") as f:
        return Config(yaml.safe_load(f))
