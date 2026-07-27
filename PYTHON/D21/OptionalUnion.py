# Optional Union

from typing import Optional, Union

class OptionalUnion:
    @staticmethod
    def parse_identifier(identifier: Union[int, str]) -> str:
        """Accepts either an integer or string ID and returns it standardized as a string."""
        return f"ID-{str(identifier).zfill(4)}"

    @staticmethod
    def find_user_profile(user_id: int) -> Optional[str]:
        """Simulates a database lookup that returns a username if found, otherwise None."""
        database = {1: "Alice", 2: "Bob"}
        return database.get(user_id, None)

    @staticmethod
    def calculate_tax(amount: float, tax_rate: Optional[float] = None) -> float:
        """Calculates tax. If tax_rate is not provided (None), defaults to 5%."""
        rate = tax_rate if tax_rate is not None else 0.05
        return amount * rate

# --- Sample Execution ---
if __name__ == "__main__":
    print("\n--- Optional & Union Typing Demo ---")
    print("Parsed ID (Int):", OptionalUnion.parse_identifier(42))
    print("Parsed ID (Str):", OptionalUnion.parse_identifier("99"))
    
    print("User Found:", OptionalUnion.find_user_profile(1))
    print("User Missing:", OptionalUnion.find_user_profile(99))
    
    print("Tax with default rate:", OptionalUnion.calculate_tax(100.0))
    print("Tax with custom rate:", OptionalUnion.calculate_tax(100.0, 0.15))