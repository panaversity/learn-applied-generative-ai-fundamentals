# Nvidia Datacenter GPUs

NVIDIA offers a variety of GPUs that are widely available for cloud computing through various cloud service providers. Here’s a list of some of the key NVIDIA GPUs that you can use in the cloud right now:

### NVIDIA GPUs for Cloud Computing

1. **NVIDIA A100**
   - **Description:** Part of the Ampere architecture, the A100 GPU is designed for high-performance computing, AI, and data analytics.
   - **Features:** Tensor cores for AI training and inference, multi-instance GPU capability.
   - **Cloud Providers:** Available on platforms like AWS (EC2 P4 instances), Google Cloud (A2 instances), and Microsoft Azure (ND A100 v4 series).

2. **NVIDIA V100**
   - **Description:** Based on the Volta architecture, the V100 is aimed at AI, deep learning, and high-performance computing.
   - **Features:** Tensor cores, high memory bandwidth, optimized for AI and HPC workloads.
   - **Cloud Providers:** Available on AWS (EC2 P3 instances), Google Cloud (V100 instances), and Microsoft Azure (NDv2 series).

3. **NVIDIA T4**
   - **Description:** Turing architecture GPU optimized for inferencing workloads, as well as training and graphics.
   - **Features:** Tensor cores, multi-precision capabilities, energy efficiency.
   - **Cloud Providers:** Available on AWS (EC2 G4 instances), Google Cloud (T4 instances), and Microsoft Azure (NVv4 series).

4. **NVIDIA K80**
   - **Description:** Kepler architecture GPU designed for general-purpose GPU computing.
   - **Features:** Dual-GPU architecture, large memory capacity.
   - **Cloud Providers:** Available on AWS (EC2 P2 instances) and Google Cloud (K80 instances).

5. **NVIDIA P100**
   - **Description:** Part of the Pascal architecture, the P100 GPU is designed for HPC and AI applications.
   - **Features:** High memory bandwidth, NVLink for fast GPU-GPU communication.
   - **Cloud Providers:** Available on Google Cloud (P100 instances) and AWS (older P2 instances).

6. **NVIDIA P4**
   - **Description:** Pascal architecture GPU optimized for inferencing and low-power, high-efficiency deployments.
   - **Features:** Tensor cores, energy efficiency, compact form factor.
   - **Cloud Providers:** Available on Google Cloud (P4 instances) and AWS (EC2 G4 instances).

7. **NVIDIA M60**
   - **Description:** Maxwell architecture GPU designed for virtual desktop infrastructure (VDI) and professional graphics.
   - **Features:** High graphics performance, multi-user support.
   - **Cloud Providers:** Available on AWS (G3 instances) and other VDI services.

### Summary of Cloud Providers Offering NVIDIA GPUs

- **Amazon Web Services (AWS):**
  - **Instances:** EC2 P4, P3, P2, G4, G3
- **Google Cloud Platform (GCP):**
  - **Instances:** A2, V100, T4, K80, P100, P4
- **Microsoft Azure:**
  - **Instances:** ND A100 v4, NDv2, NVv4

### Considerations

- **Use Case:** Choose the GPU based on your specific requirements, such as training (A100, V100), inference (T4, P4), or a mix of tasks.
- **Performance and Cost:** Higher-end GPUs like the A100 and V100 offer more performance but come at a higher cost. Mid-range options like the T4 provide a balance of performance and cost, especially for inference tasks.
- **Provider Availability:** Ensure the chosen GPU is available with your preferred cloud provider and region.

Using these GPUs in the cloud allows you to leverage powerful AI and HPC capabilities without the need for substantial upfront investment in hardware, enabling scalable and flexible computing resources.

## The Latest NVIDIA Blackwell Platform

**[NVIDIA Blackwell Platform Arrives to Power a New Era of Computing](https://nvidianews.nvidia.com/news/nvidia-blackwell-platform-arrives-to-power-a-new-era-of-computing)**

The **NVIDIA Blackwell platform** is a groundbreaking advancement in computing. It enables organizations to build and run real-time generative AI on trillion-parameter large language models (LLMs) at up to **25x less cost and energy consumption** than its predecessor. Here are the key features:

1. **Blackwell GPU Architecture**: The Blackwell GPU architecture incorporates six transformative technologies for accelerated computing. These innovations will help unlock breakthroughs in data processing, engineering simulation, electronic design automation, computer-aided drug design, quantum computing, and generative AI¹.

2. **Trillion-Parameter LLMs**: Blackwell empowers real-time generative AI using massive LLMs with **trillion parameters**. This capability is crucial for natural language understanding, text generation, and other AI tasks.

3. **Widespread Adoption**: Major cloud providers (including Amazon Web Services, Google, and Microsoft), server manufacturers, and leading AI companies are expected to adopt Blackwell. For instance, Google plans to leverage Blackwell's capabilities across its services and cloud infrastructure¹.

4. **Energy Efficiency**: Blackwell significantly reduces the operating cost and energy consumption for LLM inference, making it an environmentally friendly choice for AI workloads¹.

As for the GPU itself, the Blackwell platform features a new graphics processing unit (GPU) that NVIDIA calls the **GB200**. It's hailed as the "world's most powerful chip" for AI applications. 

## Blackwell Plastfrom Offered by Cloud Providers

The **NVIDIA Blackwell platform** is set to revolutionize computing, and several major cloud providers have already announced their plans to offer access to it:

1. **Amazon Web Services (AWS)**: AWS will provide access to the Blackwell platform, featuring the **GB200 NVL72** GPU with 72 Blackwell GPUs and 36 Grace CPUs interconnected by fifth-generation NVLink. Additionally, EC2 instances featuring the new **B100 GPUs** will be deployed in EC2 UltraClusters, and GB200s will be available on Nvidia's DGX Cloud within AWS.

2. **Google Cloud**: Google is adopting the Blackwell platform for various internal deployments and will be one of the first cloud providers to offer Blackwell-powered instances. They also offer the Nvidia H100-powered DGX Cloud platform, which is now generally available on Google Cloud. In the future, Google Cloud plans to bring Nvidia GB200 NVL72 systems (combining 72 Blackwell GPUs and 36 Grace CPUs) to its cloud infrastructure.

3. **Microsoft Azure**: Microsoft has also committed to offering access to Blackwell GPUs through its Azure cloud platform at launch.

4. **Oracle Cloud Infrastructure (OCI)**: Oracle plans to offer Nvidia's Blackwell GPUs via its OCI Supercluster and OCI Compute instances. OCI Compute will adopt both the Nvidia GB200 Grace Blackwell Superchip and the Nvidia Blackwell B200 Tensor Core GPU. Access will be available through GB200 NVL72-based instances¹.

These cloud providers recognize the transformative potential of Blackwell and are eager to integrate it into their services. Exciting times ahead for generative AI! 