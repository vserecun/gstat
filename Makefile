.PHONY: default requirements help

default: help

requirements: ## installs requirents from requiremrnts.txt file
	@pip3.7 install -r requirements.txt

help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'