ARG FEDORA_MAJOR_VERSION="${FEDORA_MAJOR_VERSION:-latest}"

FROM registry.fedoraproject.org/fedora:${FEDORA_MAJOR_VERSION} AS builder

ENV OUTPUT_ROOT=/app/output

WORKDIR /app 

ADD . /app

RUN dnf install \
    --disablerepo='*' \
    --enablerepo='fedora,updates' \
    --setopt install_weak_deps=0 \
    --nodocs \
    --assumeyes \
    'dnf-command(builddep)' \
    rpkg \
    rpm-build && \
    mkdir -p $OUTPUT_ROOT/{,output,atomic-studio/rpms} && \
    rpkg spec --outdir  "$OUTPUT_ROOT" && \
    dnf builddep -y output/studio-cli.spec && \
    rpkg local --outdir "$OUTPUT_ROOT/output" && \
    mv ${OUTPUT_ROOT}/output/noarch/* "${OUTPUT_ROOT}/atomic-studio/rpms"

FROM scratch

ENV OUTPUT_ROOT=/app/output
COPY --from=builder ${OUTPUT_ROOT}/atomic-studio/rpms /rpms
