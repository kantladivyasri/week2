import { useState } from 'react'
import AudioUploader from '../components/AudioUploader'
import TranscriptCard from '../components/TranscriptCard'
import IntentTags from '../components/IntentTags'
import EfficiencyGauge from '../components/EfficiencyGauge'
import { TranscriptionResponse } from '../types/api'

const Dashboard = () => {
  const [transcriptionResult, setTranscriptionResult] = useState<TranscriptionResponse | null>(null)
  const [error, setError] = useState<string | null>(null)

  const handleTranscriptionComplete = (result: TranscriptionResponse) => {
    setTranscriptionResult(result)
    setError(null)
  }

  const handleError = (errorMessage: string) => {
    setError(errorMessage)
    setTranscriptionResult(null)
  }

  return (
    <div className="dashboard">
      <div className="dashboard-container">
        <section className="upload-section">
          <h2>Upload Audio File</h2>
          <AudioUploader
            onTranscriptionComplete={handleTranscriptionComplete}
            onError={handleError}
          />
          {error && (
            <div className="error-message">
              <p>Error: {error}</p>
            </div>
          )}
        </section>

        {transcriptionResult && (
          <section className="results-section">
            <div className="results-grid">
              <div className="result-card">
                <TranscriptCard transcript={transcriptionResult.transcript} />
              </div>
              <div className="result-card">
                <IntentTags intents={transcriptionResult.intents} />
              </div>
              <div className="result-card">
                <EfficiencyGauge efficiency={transcriptionResult.efficiency} />
              </div>
            </div>
            {transcriptionResult.processing_time && (
              <div className="processing-info">
                <p>Processing time: {transcriptionResult.processing_time}s</p>
              </div>
            )}
          </section>
        )}
      </div>
    </div>
  )
}

export default Dashboard

