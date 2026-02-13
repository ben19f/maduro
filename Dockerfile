FROM ubuntu:latest
LABEL authors="ben"

ENTRYPOINT ["top", "-b"]