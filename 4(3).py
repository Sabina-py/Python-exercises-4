nums = []

while True:
    entry = input("Enter a number (empty to stop): ")
    if entry == "":
        break
    nums.append(float(entry))

if nums:
    print(f"Smallest number: {min(nums)}")
    print(f"Largest number: {max(nums)}")
else:
    print("No numbers entered.")
