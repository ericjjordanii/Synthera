from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PROJECT = ROOT / "projects" / "SYN-P001-EJJoftheCloud"
AGENTS = PROJECT / "agents"
DEPLOYMENTS = PROJECT / "deployments" / "chatgpt"


EXPECTED = {
    "SYN-P001-A001": ("COMMAND_CENTER.md", "COMMAND_CENTER.md"),
    "SYN-P001-A002": ("TECHNICAL_CURRICULUM.md", "TECHNICAL_CURRICULUM.md"),
    "SYN-P001-A003": ("CLOUD_CONSULTANT.md", "CLOUD_CONSULTANT.md"),
    "SYN-P001-A004": ("CONTENT_STUDIO.md", "CONTENT_STUDIO.md"),
    "SYN-P001-A005": ("PROOF_OF_WORK.md", "PROOF_OF_WORK.md"),
}


def test_core_agent_deployment_coverage():
    registry = (DEPLOYMENTS / "registry.yaml").read_text()
    for agent_id, (canonical_file, deployment_file) in EXPECTED.items():
        assert (AGENTS / canonical_file).exists()
        assert (DEPLOYMENTS / deployment_file).exists()
        assert agent_id in registry
        assert agent_id in (AGENTS / canonical_file).read_text()
