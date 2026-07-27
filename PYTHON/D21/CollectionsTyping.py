# Collections Typing

from typing import List, Dict, Tuple, Set, Sequence, Mapping

class CollectionsTyping:
    @staticmethod
    def process_scores(scores: List[int]) -> float:
        """Takes a list of integers and returns the average as a float."""
        if not scores:
            return 0.0
        return sum(scores) / len(scores)

    @staticmethod
    def get_user_metadata(user_id: int) -> Tuple[str, int, bool]:
        """Returns a fixed-size tuple containing (username, age, is_active)."""
        return ("alice_99", 28, True)

    @staticmethod
    def count_item_frequencies(items: Sequence[str]) -> Dict[str, int]:
        """Counts occurrences of each item in a sequence and returns a dictionary."""
        freq: Dict[str, int] = {}
        for item in items:
            freq[item] = freq.get(item, 0) + 1
        return freq

    @staticmethod
    def get_unique_tags(tags: Set[str]) -> Set[str]:
        """Processes and returns a set of unique string tags in uppercase."""
        return {tag.upper() for tag in tags}

# --- Sample Execution ---
if __name__ == "__main__":
    print("--- Collections Typing Demo ---")
    print("Average Score:", CollectionsTyping.process_scores([85, 90, 78, 92]))
    print("User Metadata:", CollectionsTyping.get_user_metadata(101))
    print("Frequencies:", CollectionsTyping.count_item_frequencies(["apple", "banana", "apple"]))
    print("Unique Tags:", CollectionsTyping.get_unique_tags({"python", "coding", "python"}))

    