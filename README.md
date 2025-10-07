# ml-catalyst-project
An open, machine-learning–driven computational framework that automatically extracts and quantifies atomic-scale dynamics from electron microscopy and atomistic simulations to reveal how catalysts evolve under working conditions.
AtomML: Automated Atomic-Scale Catalyst Dynamics Analysis

An open, machine-learning–driven computational framework for extracting and quantifying atomic-scale dynamics from electron microscopy and simulations.

Overview:

AtomML provides a reproducible pipeline for analyzing atomic motion and structural dynamics in catalysts under working conditions.
It combines open electron microscopy analysis tools, machine learning, and atomistic simulations (MD/DFT) to bridge the gap between experimentally observed atomic motion and chemical driving forces.

Inspired by Topsoe’s atomic-scale catalyst research (Helveg et al.), this project demonstrates how publicly available data and computational methods can be used to extract fundamental insights into catalyst behavior — without specialized hardware.

Key Features:

- Automated atomic detection & tracking from STEM/TEM images using:

    Classical Gaussian fitting (Atomap)

    Machine learning (custom U-Net detector)

- Atomic trajectory reconstruction & mobility mapping

    Per-atom displacement, diffusion, and uncertainty quantification

- Forward simulation of microscopy data using abTEM

    Generate realistic STEM images from MD or DFT snapshots

- Atomistic modeling integration

    Link observed mobility to coordination, potential energy, and binding energies via ASE, LAMMPS, or GPAW

- Chemically meaningful visualization

    Heatmaps of atomic mobility, local energy correlations, and uncertainty overlays

- Reproducible Python pipeline

    Fully Jupyter-notebook compatible, built with open-source tools

Scientific Motivation:

Catalysts are not static — their active sites evolve dynamically under operating conditions.
Topsoe and Stig Helveg’s research has shown this experimentally using in situ electron microscopy.
AtomML complements that work computationally by providing:

Automated, open-source analysis of atomic-scale motion

Simulation-based validation of experimental observations

Chemically interpretable links between dynamics and energetics

In short, AtomML is to atomic-resolution microscopy what autoXAS is to operando spectroscopy.
