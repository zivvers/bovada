
FROM continuumio/miniconda3
MAINTAINER ziv@uchicago.edu

# install sudo in anticipation of less-privledged user
RUN apt-get -qqy update && \
    apt-get -qqy install sudo

# make less-privleged user
ENV CONDA_CALLER=ana

RUN useradd -s /bin/bash $CONDA_CALLER

# give CONDA_CALLER sudo privledges
RUN echo "$CONDA_CALLER ALL=(ALL) NOPASSWD:ALL" > /etc/sudoers.d/notebook

# install Selenium!
RUN conda install -yqc conda-forge selenium
#RUN conda install python=3.5
COPY requirements.txt .

#RUN conda install -y notebook
RUN conda install -y --file requirements.txt 
RUN conda install -yc conda-forge gspread
RUN conda install -yc conda-forge oauth2client


USER $CONDA_CALLER
WORKDIR /home/$CONDA_CALLER
