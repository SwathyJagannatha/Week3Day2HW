#2. Set Operations in Data Analysis

customer_ids = ["C001", "C002", "C003", "C002", "C001", "C004"]
new_ids=["A123","B345","A123","B678","U789","U789","B678","A123","A123"]

def print_unique(customer_ids):

    unique_id = set(customer_ids)
    print(unique_id)


def main(unique_id):
    print("Hello, This is the set of unique customer id...without duplicates")
    print_unique(unique_id)

#main(customer_ids)
main(new_ids)