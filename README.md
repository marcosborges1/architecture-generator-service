# Architecture Generator (AG)

## Overview

The Architecture Generator (AG) is the main component of our approach, playing a crucial role in creating SoS architectures in the System Entity Structure (SES) language, which was designed to detail the decomposition of systems into subsystems based on a given perspective, and how such subsystems interact with each other. The AG generates the SES architecture using information from the JSON files missionFileJson and cssBehaviorFileJson, which are produced by the other two components, ME and CBA, respectively.

The essence of AG's functionality is rooted in the [Algorithm section](#Algorithm).

## Algorithm

The AG's core is based on the algorithm described below.

<img src="/images/ag_algorithm.png" height="300"/>

## Implementation Details

Constructed using Python, the AG service is a lightweight, dynamic, and web-compatible solution. The choice of language complements the ME algorithm's versatility and caters to the overarching requirements of the System of Systems context.

## Setup

Before running the application, make sure to install the required dependencies. You can install them using `pip`:

```bash
pip install -r requirements.txt
```

## Usage

Before you start the AG, be sure to start it.

```bash
python server.py
```

Access the AG from the GraphQL endpoint:

```bash
http://localhost:4003/graphql
```

**Note**:

- The default PORT is _4003_, but can be change for your convenience.
- This project heavily relies on GraphQL, a powerful query language for APIs, and a server-side runtime for executing those queries with your existing data. If you're unfamiliar with GraphQL or wish to dive deeper, you can [learn more about GraphQL here](https://graphql.org/).

<!-- ## References -->

## Project Status

The AG, currently in the evolutionary phase. It is actively undergoing improvements and changes to refine its capabilities and more effectively meet new requirements.

## Author

**Marcos Borges**  
PhD Student at Federal University of Ceará, Brazil  
Email: [marcos.borges@alu.ufc.br](mailto:marcos.borges@alu.ufc.br)

## Contributing

Community-driven improvements are always welcome. If you're looking to contribute, feel free to raise pull requests. For more significant changes or additions, it's recommended to open an issue first for discussions.

## License

This project is licensed under the GPL-3.0 License - see the [LICENSE](LICENSE) file for details.
