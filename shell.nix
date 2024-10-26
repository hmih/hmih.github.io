{ pkgs ? import <nixpkgs> {} }:

pkgs.mkShellNoCC {
  buildInputs = with pkgs; [
    # --pure
    git
    gnumake
    clang
    openssh

    python3
    python3Packages.pelican
    ghp-import
  ];
}
