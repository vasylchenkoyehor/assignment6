<!DOCTYPE html>
<html>
<head>
    <title>Integer Input Form</title>
</head>
<body>
    <h1>Enter Integers and Threshold</h1>
    <form action="process.php" method="get">
        <label for="integers">Enter integers (comma-separated):</label><br>
        <input type="text" id="integers" name="integers" placeholder="e.g., 3,5,7,9"><br><br>
        <label for="threshold">Enter threshold:</label><br>
        <input type="text" id="threshold" name="threshold" placeholder="e.g., 4"><br><br>
        <button type="submit">Submit</button>
    </form>
</body>
</html>
