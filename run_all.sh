#!/usr/bin/env bash
# Runs the four independent checks of the identities of the paper on small cases.
# Requirements: python3, julia, a C compiler, a C++17 compiler.
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
BUILD="$(mktemp -d)"
trap 'rm -rf "$BUILD"' EXIT
CC_BIN="${CC:-cc}"
CXX_BIN="${CXX:-c++}"

step() { printf '\n=== %s\n' "$1"; }

for tool in python3 julia "$CC_BIN" "$CXX_BIN"; do
  command -v "$tool" >/dev/null 2>&1 || { echo "missing tool: $tool" >&2; exit 2; }
done

step "Python"
python3 -I "$ROOT/checks/python/check.py"
python3 -I "$ROOT/checks/python/proof_steps.py"

step "Julia"
julia "$ROOT/checks/julia/check.jl"

step "C"
"$CC_BIN" -O2 -o "$BUILD/check_c" "$ROOT/checks/c/check.c"
"$BUILD/check_c"

step "C++"
"$CXX_BIN" -O2 -std=c++17 -o "$BUILD/check_cpp" "$ROOT/checks/cpp/check.cpp"
( cd "$ROOT/checks/cpp" && "$BUILD/check_cpp" )

printf '\nAll steps passed.\n'
