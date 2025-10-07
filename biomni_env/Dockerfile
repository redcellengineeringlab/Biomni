FROM continuumio/miniconda3

# create the env
COPY agent_env.yml .
RUN conda env create -f agent_env.yml

# make RUN commands use the new env
SHELL ["conda", "run", "-n", "biomni_e1", "/bin/bash", "-c"]
