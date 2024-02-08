# main.py

import hydra
from omegaconf import DictConfig
from src.train import train_model

@hydra.main(config_path="conf/config.yaml")
def main(config: DictConfig) -> None:
    train_model(config)

if __name__ == "__main__":
    main()
