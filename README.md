![](https://i.imgur.com/u3bvu9n.png)
# oxkat

<b>"Ceci n'est pas une pipe[line]"</b><br> 
(_The Treachery of Images_, René Magritte, 1929)

---

## What is this?

* A set of Python scripts with the aim of (semi-)automatically processing [MeerKAT](https://www.sarao.ac.za/science-engineering/meerkat/) data. 


* At the core is a set of functions that generate calls to [various pieces](README.md#software-package-roll-call) of radio astronomy software, a semi-modular bunch of CASA scripts for performing reference calibration, and a fairly sizeable list of default parameters (at present suitable for full L-band Stokes-I continuum imaging).


* Job script generation and dependency chains are automatically handled when running on the [ilifu/IDIA](https://www.idia.ac.za/) cluster, UKZN's [hippo](https://astro.ukzn.ac.za/~hippo/) cluster, or the [CHPC](https://www.chpc.ac.za/)'s [Lengau](https://www.chpc.ac.za/index.php/resources/lengau-cluster) cluster.


* Setup scripts glue the above components together into a processing recipe. The default procedure is broken down into stages, after each of which it is advisable to pause and examine the state of the process before continuing.  


* The intention is that the bar to entry is low. If you have stock Python then nothing else needs installing apart from [Singularity](https://singularity.lbl.gov/), which is available on both the ilifu/IDIA and CHPC clusters, in which case all the underlying radio astronomy packages are containerised. The Singularity layer can also be disabled for running packages on your own machine, either directly, or inside a Python virtual environment.


* Please file bugs, suggestions, questions, etc. as [issues](https://github.com/IanHeywood/oxkat/issues).


---

## Quick start

1. If you have your [containers all set up](README.md#getting-containers) then log into your machine or cluster, e.g.:

   ```
   $ ssh ianh@slurm.ilifu.ac.za
   ```

2. Navigate to a working area / scratch space:

   ```
   $ cd /scratch/users/ianh/XMM12
   ```

3. Clone the root contents of this repo into it:

   ```
   $ git clone https://github.com/IanHeywood/oxkat.git .
   ```

4. Make a symlink to your MeerKAT Measurement Set (or place it in the working folder, it will not be modified at all):

   ```
   $ ln -s /idia/projects/mightee/1538856059/1538856059_sdp_l0.full_1284.full_pol.ms .
   ```

5. Generate and submit (or run) the jobs required for the reference calibration (1GC):

   ```
   $ python setups/1GC.py <idia|hippo|chpc|node>
   $ ./submit_1GC_jobs.sh
   ```

6. If something goes wrong you can kill the running and queued jobs on a cluster with:

   ```
   $ source SCRIPTS/kill_1GC_jobs.sh
   ```

7. Once this has completed then examine the products, and move to the next steps in the same fashion. 

Please see the [setups README](setups/README.md) for more details. Most of the settings can be tuned via the [`config.py`](oxkat/config.py) file. Note that for use on a cluster you might have to load a `python3` module. On the IDIA cluster this is achieved with:

   ```
   $ module load anaconda3
   ```

which you can also add to your `~/.bashrc` file for simplicity.

---

## Getting containers

Singularity can be used to download and build containers from [Docker Hub](https://hub.docker.com/). There is a [script](https://github.com/IanHeywood/oxkat/blob/master/tools/pull_containers.sh) included to download them for you. [@SpheMakh](https://github.com/sphemakh)'s [stimela](https://hub.docker.com/u/stimela) project maintains containers for most radio astronomy applications, and repository of pre-built containers is now available at both IDIA and CHPC (in support of the [`CARACal`](https://github.com/caracal-pipeline) software).

The default container paths are specified in the [`config.py`](oxkat/config.py) file. The scripts will select the required containers via pattern matching so if a container is replaced with a newer version it should be seamless.

The IDIA slurm head node does not have singularity available, so if you are pulling your own containers that must be done either via a standalone node or a worker node, or otherwise copied over via the `transfer.ilifu.ac.za` node. You will not be able to use the `pull_containers.sh` script on the Lengau head node, and the worker nodes at CHPC do not have external connectivity, so you will have to build the containers elsewhere and then transfer them to CHPC via their `scp.chpc.ac.za` node.

---

## Software package roll-call

If you are publishing results that have made use of `oxkat` then [please cite the ACSL entry](https://ui.adsabs.harvard.edu/abs/2020ascl.soft09003H/abstract), and (more importantly) the references to any underlying packages used.

| Package | Stage | Purpose | Reference |
| --- | --- | --- | --- | 
| [`CASA`](https://casa.nrao.edu/) | 1GC, 2GC | Averaging, splitting, cross calibration, DI self-calibration, flagging | [McMullin et al., 2007](https://ui.adsabs.harvard.edu/abs/2007ASPC..376..127M/abstract)|
| [`CubiCal`](https://github.com/ratt-ru/CubiCal) | 3GC | DI / DD self-calibration | [Kenyon et al., 2018](https://ui.adsabs.harvard.edu/abs/2018MNRAS.478.2399K/abstract)|
| [`DDFacet`](https://github.com/saopicc/DDFacet) | 3GC | Imaging with direction-dependent corrections | [Tasse et al., 2018](https://ui.adsabs.harvard.edu/abs/2018A%26A...611A..87T/abstract) | 
| [`killMS`](https://github.com/saopicc/killMS) | 3GC | DD self-calibration| - |
| [`PyBDSF`](https://www.astron.nl/citt/pybdsf/) | 3GC | Source finding | [Mohan & Rafferty, 2017](https://ui.adsabs.harvard.edu/abs/2015ascl.soft02007M/abstract) |
| [`owlcat`](https://github.com/ska-sa/owlcat/) | 2GC, 3GC |FITS file manipulation | - |
| [`ragavi`](https://github.com/ratt-ru/ragavi/) | 1GC, 2GC | Plotting gain solutions| - |
| [`shadeMS`](https://github.com/ratt-ru/shadeMS/) | 1GC | Plotting visibilities| - |
| [`tricolour`](https://github.com/ska-sa/tricolour) | FLAG | Flagging | - |
| [`wsclean`](https://sourceforge.net/p/wsclean/wiki/Home/) | FLAG, 2GC, 3GC | Imaging, model prediction | [Offringa et al., 2014](https://ui.adsabs.harvard.edu/abs/2014MNRAS.444..606O/abstract)|

---

Thank you for visiting.


