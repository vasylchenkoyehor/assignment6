<?php

// Get inputs from the form or URL parameters
$integers = isset($_GET['integers']) ? $_GET['integers'] : '';
$threshold = isset($_GET['threshold']) ? $_GET['threshold'] : '';

if (empty($integers) || empty($threshold)) {
    echo "<h3>Error:</h3><p>Please provide both integers and a threshold value.</p>";
    exit();
}

// Escape inputs for shell safety
$escaped_integers = escapeshellarg($integers);
$escaped_threshold = escapeshellarg($threshold);

// Call the Python script
$output = shell_exec("python3 bitwise_operations.py $escaped_integers $escaped_threshold");

if ($output === null) {
    echo "<h3>Error:</h3><p>There was an issue running the Python script.</p>";
} else {
    // Display results in HTML
    echo "<html><body>";
    echo "<h3>Results:</h3>";
    $output_lines = explode("\n", trim($output));
    foreach ($output_lines as $line) {
        echo "<p>" . htmlspecialchars($line) . "</p>";
    }
    echo "</body></html>";
}
?>
