VERSION 0.8
PROJECT atomic-studio-org/cli 

studio-cli:
	FROM registry.fedoraproject.org/fedora-toolbox

	RUN dnf -y install dnf-plugins-core \
		&& dnf install --refresh -y \
			jq \
			docker-ce \
			docker-ce-cli \
			containerd.io \
			docker-buildx-plugin \
			docker-compose-plugin \
			buildah \
			podman \
			skopeo \
			distrobox

	COPY +cosign/cosign /usr/bin/cosign

	COPY (+install/bluebuild --BUILD_TARGET="x86_64-unknown-linux-gnu" --NIGHTLY=$NIGHTLY) /usr/bin/bluebuild

	ARG TAG
	ARG LATEST=false

	RUN mkdir -p /bluebuild
	WORKDIR /bluebuild
	ENTRYPOINT ["bluebuild"]

	DO cargo+SAVE_IMAGE --IMAGE=$IMAGE --TAG=$TAG --LATEST=$LATEST --NIGHTLY=$NIGHTLY

cosign:
	FROM gcr.io/projectsigstore/cosign
	SAVE ARTIFACT /ko-app/cosign
