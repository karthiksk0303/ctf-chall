<?php
class FileGate {
    public $file = "guest_log.txt";
    function __destruct() {
        include($this->file);
    }
}

if (isset($_GET['data'])) {
    unserialize($_GET['data']);
} else {
    echo "Internal Logging System Active.";
}
?>
