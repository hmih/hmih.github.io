{ pkgs ? import <nixpkgs> {} }:

pkgs.mkShellNoCC {
  buildInputs = with pkgs; [
    # --pure
    git
    gnumake
    jekyll
    bundler
    clang
  ];
}
