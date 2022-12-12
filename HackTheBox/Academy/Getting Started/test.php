<?php 
    $output = shell_exec('ls -la 2>&1');
    echo "<pre>$output</pre>"
;?>