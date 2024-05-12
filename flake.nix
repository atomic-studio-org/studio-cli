{
  description = "Atomic Studio CLI";

  inputs.nixpkgs.url = "github:nixos/nixpkgs/nixpkgs-unstable";

  outputs = { self, nixpkgs }:
    let
      supportedSystems = [ "x86_64-linux" "aarch64-linux" ];
      forEachSupportedSystem = f: nixpkgs.lib.genAttrs supportedSystems (system: f {
        pkgs = import nixpkgs { inherit system; };
      });
    in
    {
      formatter = forEachSupportedSystem ({ pkgs }: pkgs.nixfmt-rfc-style);

      packages = forEachSupportedSystem ({ pkgs }: rec {
        default = studio;
        studio = pkgs.stdenvNoCC.mkDerivation rec {
          pname = "studio";
          name = "studio";
          src = pkgs.lib.cleanSource ./.;

          buildInputs = with pkgs; [ podman distrobox ];

          buildCommand = ''
            mkdir -p $out/bin $out/libexec
            cp $src/src/${pname} $out/bin
            substituteInPlace $out/bin/${pname} --replace './libexec' "$out/libexec"
            cp -r $src/src/libexec/* $out/libexec
          '';
        };
      });

      devShells = forEachSupportedSystem ({ pkgs }: {
        default = pkgs.mkShell {
          packages = with pkgs; [ earthly go-task melange apko rpm ];
        };
      });
    };
}
