import React, { useState, useEffect } from "react";
import "./Iam.css";
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faUpload, faCheckCircle, faExclamationCircle, faSpinner, faDownload, faUsersGear, faFileCsv } from '@fortawesome/free-solid-svg-icons';

const User = () => {
  const [csvFile, setCsvFile] = useState(null);
  const [storedFile, setStoredFile] = useState(null);
  const [processing, setProcessing] = useState(false);
  const [apiStatus, setApiStatus] = useState(null);
  const [downloadReady, setDownloadReady] = useState(false);
  const [processedCount, setProcessedCount] = useState(0);
  const [showFeatures, setShowFeatures] = useState(false);
  const [showSteps, setShowSteps] = useState(false);
  const [errorMsg, setErrorMsg] = useState("");

  useEffect(() => {
    const count = parseInt(localStorage.getItem('processedFiles') || '0');
    setProcessedCount(count);
  }, []);

  const handleFileChange = (e) => {
    setCsvFile(e.target.files[0]);
    setApiStatus(null);
    setDownloadReady(false);
  };

  const handleDragOver = (e) => {
    e.preventDefault();
    e.currentTarget.classList.add('dragover');
  };

  const handleDragLeave = (e) => {
    e.currentTarget.classList.remove('dragover');
  };

  const handleDrop = (e) => {
    e.preventDefault();
    e.currentTarget.classList.remove('dragover');
    const files = e.dataTransfer.files;
    if (files.length > 0 && files[0].name.endsWith('.csv')) {
      setCsvFile(files[0]);
      setApiStatus(null);
      setDownloadReady(false);
    }
  };

  const handleProceed = async () => {
    if (csvFile) {
      setProcessing(true);
      setApiStatus(null);
      setDownloadReady(false);
      setErrorMsg(""); // Reset error message

      try {
        const formData = new FormData();
        formData.append('file', csvFile);

        const response = await fetch('http://127.0.0.1:5000/User', {
          method: 'POST',
          body: formData,
        });

        const data = await response.json();
        if (data.status) {
          setStoredFile(csvFile);
          setApiStatus("success");
          setDownloadReady(true);
          const newCount = processedCount + 1;
          setProcessedCount(newCount);
          localStorage.setItem('processedFiles', newCount.toString());
        } else {
          setApiStatus("error");
          setErrorMsg(data.error || "Unknown error occurred while processing the file.");
        }
      } catch (error) {
        setApiStatus("error");
        setErrorMsg(error.message || "Network error. Please try again.");
      } finally {
        setProcessing(false);
      }
    }
  };

  const handleDownload = async () => {
    if (apiStatus === "success" && storedFile) {
      try {
        const response = await fetch('http://127.0.0.1:5000/download/user_report.csv');
        if (response.ok) {
          const blob = await response.blob();
          const url = window.URL.createObjectURL(blob);
          const a = document.createElement('a');
          a.href = url;
          a.download = 'user_report.csv';
          document.body.appendChild(a);
          a.click();
          a.remove();
          window.URL.revokeObjectURL(url);
        } else {
          alert("Report file not found on server.");
        }
      } catch (error) {
        alert("Failed to download report.");
      }
    } else {
      alert("Report not available. Please process a file first.");
    }
  };

  return (
    <div className="group-container">
      <div className="header">
        <h1>
          <FontAwesomeIcon icon={faUsersGear} style={{ color: "#667eea", marginRight: "10px" }} />
          AWS IAM User Management Dashboard
        </h1>
        <p>Streamline your AWS Identity and Access Management with advanced CSV processing</p>
      </div>

      <div className="card main-card">
        <div className="card-header">
          <div className="card-icon">
            <FontAwesomeIcon icon={faFileCsv} style={{ color: "#059669", fontSize: "1.6rem" }} />
          </div>
          <div className="card-title">AWS IAM User Processing</div>
        </div>

        <div 
          className="file-upload-area" 
          onClick={() => document.getElementById('csvFile').click()}
          onDragOver={handleDragOver}
          onDragLeave={handleDragLeave}
          onDrop={handleDrop}
        >
          <span className="upload-icon">
            <FontAwesomeIcon icon={faUpload} />
          </span>
          <span className="upload-text">Upload Your CSV File</span>
          <span className="upload-subtext">Drag and drop your file here or click to browse (Only .csv files accepted)</span>
          <input
            id="csvFile"
            type="file"
            accept=".csv"
            className="file-input"
            onChange={handleFileChange}
            disabled={processing}
          />
        </div>

        {csvFile && (
          <div className="file-name">Selected: {csvFile.name}</div>
        )}

        <div className="button-group">
          <button
            className="primary-button"
            onClick={handleProceed}
            disabled={!csvFile || processing}
          >
            {processing ? (
              <>
                <div className="button-spinner">
                  <FontAwesomeIcon icon={faSpinner} spin />
                </div>
                Processing...
              </>
            ) : (
              <>Process File</>
            )}
          </button>
          {downloadReady && (
            <button
              className="download-button"
              onClick={handleDownload}
            >
              <FontAwesomeIcon icon={faDownload} />
              Download group_report.csv
            </button>
          )}
        </div>

        <div className={`status-card${processing ? " processing" : ""}`}>
          {processing && (
            <>
              <div className="spinner">
                <FontAwesomeIcon icon={faSpinner} spin />
              </div>
              <h3>Processing...</h3>
              <p className="magic-text">Please wait while we generate your report.</p>
            </>
          )}

          {apiStatus === "success" && storedFile && (
            <div className="success-message celebration">
              <span className="success-icon" role="img" aria-label="Success">
                <FontAwesomeIcon icon={faCheckCircle} />
              </span>
              <h3>File Processed Successfully!</h3>
              <p className="file-processed">Stored file: <strong>{storedFile.name}</strong></p>
              <p>Your AWS IAM group report has been generated and is ready for download.</p>
            </div>
          )}
        </div>
      </div>

      {/* Error message always visible below the card */}
      {apiStatus === "error" && (
        <div className="error-message status-card">
          <span className="error-icon" role="img" aria-label="Error">
            <FontAwesomeIcon icon={faExclamationCircle} />
          </span>
          <h3>Processing Error</h3>
          <p>
            {errorMsg
              ? errorMsg
              : "Failed to process file. Please check your CSV format and try again."}
          </p>
        </div>
      )}
    </div>
  );
};

export default User;