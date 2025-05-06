import matplotlib.pyplot as plt

# Data
# =============================================================================
# x = [10, 20, 30, 40, 50]
# y = [2.5, 3, 5, 7, 11]
# 
# # Create line plot
# plt.plot(x, y)
# plt.title("Simple Line Plot")
# plt.xlabel("X-axis- Values")
# plt.ylabel("Y-axis- Grade")
# plt.show()
# =============================================================================

# =============================================================================
# x = [1, 2, 3, 4, 5]
# y = [2, 3, 5, 7, 11]
# =============================================================================

# Create scatter plot
# =============================================================================
# plt.scatter(x, y)
# plt.title("Simple Scatter Plot")
# plt.xlabel("X-axis")
# plt.ylabel("Y-axis")
# plt.show()
# =============================================================================

categories = ['A', 'B', 'C', 'D']
values = [4, 7, 1, 8]

# Create bar chart
plt.bar(categories, values)
plt.title("Simple Bar Chart")
plt.xlabel("Categories")
plt.ylabel("Values")
plt.show()




# =============================================================================
# labels = ['A', 'B', 'C', 'D']
# sizes = [15, 30, 45, 10]
# 
# # Create pie chart
# plt.pie(sizes, labels=labels, autopct='%1.1f%%')
# plt.title("Simple Pie Chart")
# plt.show()
# =============================================================================


# =============================================================================
# data = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5]
# 
# # Create histogram
# plt.hist(data, bins=5)
# plt.title("Simple Histogram")
# plt.xlabel("Value")
# plt.ylabel("Frequency")
# plt.show()
# =============================================================================



