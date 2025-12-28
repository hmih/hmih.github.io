let
  # The hash you found from the curl command (the long or short version works)
  rev = "82367db1960027cb9dc30c435aa578d96572a29d"; 
  nixpkgs = fetchTarball {
    url = "https://github.com/NixOS/nixpkgs/archive/${rev}.tar.gz";
    sha256 = "1m2lficgadkgcz18d5n20y1dhf8n2akk0qjxv69hd3qkc0ymar58";
  };
  pkgs = import nixpkgs {};
in
pkgs.mkShellNoCC {
  buildInputs = with pkgs; [
    git
    gnumake
    clang
    openssh
    python3
    python3Packages.pelican
    python3Packages.markdown
    ghp-import
  ];
}
