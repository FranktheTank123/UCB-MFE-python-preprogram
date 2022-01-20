# Lecture 6: Productionization II

## Integration test and Regression test
- Integration test
    - data cleansing pipeline
    - model training pipeline
    - model serving
    - ...
- Regression test
    - latency & responding time
    - backtest (?)
    - ...
- reference:
    - https://www.kdnuggets.com/2019/11/testing-machine-learning-pipelines.html


## makefile
- Make your life easier
- `make lint` instead of running `flake8` +  `mypy` + ...
- `make install` <- who doesn't like 1-click setup?
- checkout `Makefile`
- Note: indentation needs to be `Tab`. It cannot be `Spaces`


## What does productionization mean?
- when your customers are going to meet your code
- [white-boarding] illustrate how customers interact with your code (while you are sleeping) 
  - example: what happens when you type www.google.com (while google engineers enjoy Saturday vacation)
    - find the ip of www.google.com -> xxx.xx.xx.xx
    - establish a TCP connection with that ip 
    - send http or https request via the connection
    - wait for response (error code + content)
  - How do we bring our ML models to the customers?


## Development Environment
- **Local/Development**: your laptop or a sandbox on a development server 
- **Testing**: for all the tests, shares the same environment as `staging` and `production`.
- **Staging**: an environment for final testing immediately prior to deploying to production. A mirror of `production`, but not facing to the users.
- **Production**: the environment that users/clients directly interact with
- [some white board illustration here]
- [CI/CD](https://www.redhat.com/en/topics/devops/what-is-ci-cd)
  - ![](https://www.redhat.com/cms/managed-files/styles/wysiwyg_full_width/s3/ci-cd-flow-desktop.png?itok=2EX0MpQZ)


## Continuous Integration
- a lot of tools out there
  - [Jenkins](https://www.jenkins.io/)
  - [CircleCI](https://circleci.com/)
  - [TravisCI](https://www.travis-ci.com/)
  - [GitHub Actions](https://github.com/features/actions)
  - paid vs. free
  - managed testing machine vs. DIY
- [GitHub Actions tutorial](https://docs.github.com/en/actions/quickstart)
  - it's repo-level
  - create `.github/workflows` folders in the repository
  - create a YAML file called `github-actions-demo.yml`
    - [YAML crash course](https://www.cloudbees.com/blog/yaml-tutorial-everything-you-need-get-started)
  - [explain the syntax a little bit]
  - [live demo] A more complex tutorial
    - `more-complex-actions.yml`
- CI in real live
  - what do we need to run every PR / merge-of-PR?
    - unit test?
    - integration test?
    - release?
    - deployment?
    - ...
  - requirements
    - only run CI when there is a code change in `Lectures/Lecture 6/code`
    - lint check
    - unit test (only run when lint check passes)
    - deployment (just print out "deploy"),  run after unit test succeed, and do not run on PR
    - it needs to have python & corresponding requirement
  - Outstanding issue
    - duplication of `pip install -r ...`
        - if we need to install some deep learning module, it will get messier
    - no guarantee that the testing environment 100% mimic production
    - **Solution**: [containerization](https://www.ibm.com/cloud/learn/containerization)
  
## Docker
- [Container vs Virtual Machine](https://www.docker.com/resources/what-container)
- [installation](https://docs.docker.com/get-started/)
- `docker run -d -p 80:80 docker/getting-started`
- docker image:
  - https://hub.docker.com/r/docker/getting-started
  - existing images, such as [python](https://hub.docker.com/_/python)
    - each tags is a version
      - `docker run -it python:3.10.1-slim-buster` (`-it` allow interactive shell)
      - `docker run -it python:3.10.1-slim-buster bash` (run `bash` instead of `python3`)
        - https://github.com/docker-library/python/blob/db32c7803dfc67e5a359514371e66d6405695e45/3.10/buster/slim/Dockerfile#L150
        - https://docs.docker.com/engine/reference/commandline/run/
  - dockerfile
    - must have name `Dockerfile`
    - `docker build code/docker_example1/ -t test`
    - `docker run -it test`
  - usually `Dockerfile` lives at the parent directory
    - `docker run -it test1`
    - `docker run -it test1` (and use `ls` to check files)
  - how to install requirements and run `make`? 
    - add `RUN pip install -r requirements.txt` and `RUN apt-get update && apt-get install -y make`
    - try `docker run test make test` and `docker run  test make lint-check`
  - GitHub Actions & Docker
    - `serious-action-with-docker`
    - build image vs. install local everytime
    - why build image is faster?
      - docker build is layer by layer
      - https://docs.docker.com/develop/develop-images/dockerfile_best-practices/
  - docker repository
    - provider
      - docker repo
      - AWS registry 
      - GCP registry
      - Ali Cloud docker registry
      - ^^ all equivalent
    - best practice:
        - build repo when PR is merged to master, as part of the CI workflow, also push that build to registry
        - deploy service, using the latest docker build
  
## Other topics if time allows
- ...
    