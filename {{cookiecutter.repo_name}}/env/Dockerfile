FROM mcr.microsoft.com/azureml/inference-base-2204:20240730.v5

ARG USER_ID
ARG USER_GROUP_ID

USER root

RUN addgroup --gid $USER_GROUP_ID ds
RUN adduser --disabled-password --gecos '' --uid $USER_ID --gid $USER_GROUP_ID  ds

#Setting a password (root) for the root user in case we needto use it with the image loaded.
RUN echo 'root:root' | chpasswd



ENV APP_DIR=/work
ENV PYTHONPATH=$APP_DIR

WORKDIR $APP_DIR

# Installing openssh
RUN apt update &&\
    apt install openssh-client -y

ENV CONDA_PREFIX=/opt/azureml-env
ENV CONDA_DEFAULT_ENV=$CONDA_PREFIX
ENV PATH=$CONDA_PREFIX/bin:$PATH
ENV PATH=${PATH}:/home/ds/.local/bin


# Create conda environment
COPY conda_environment.yml .
RUN conda env create -p $CONDA_PREFIX -f conda_environment.yml -q && \
    rm conda_environment.yml && \
    conda env list && \
    conda info --envs && \
    conda run -p $CONDA_PREFIX pip cache purge && \
    conda clean -a -y

# Installing azure cli
RUN curl -sL https://aka.ms/InstallAzureCLIDeb | bash

USER ds

RUN echo "source activate $CONDA_PREFIX" >> ~/.bashrc

ENTRYPOINT tail -f /dev/null
