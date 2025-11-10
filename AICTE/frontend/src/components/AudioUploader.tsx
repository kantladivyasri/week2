import { useState, useRef } from 'react'
import { transcribeAudio } from '../api/client'
import { TranscriptionResponse } from '../types/api'

interface AudioUploaderProps {
  onTranscriptionComplete: (result: TranscriptionResponse) => void
  onError: (error: string) => void
}

const AudioUploader = ({ onTranscriptionComplete, onError }: AudioUploaderProps) => {
  const [isUploading, setIsUploading] = useState(false)
  const [selectedFile, setSelectedFile] = useState<File | null>(null)
  const fileInputRef = useRef<HTMLInputElement>(null)

  const handleFileSelect = (event: React.ChangeEvent<HTMLInputElement>) => {
    const file = event.target.files?.[0]
    if (file) {
      setSelectedFile(file)
    }
  }

  const handleUpload = async () => {
    if (!selectedFile) {
      onError('Please select an audio file first')
      return
    }

    setIsUploading(true)
    try {
      const result = await transcribeAudio(selectedFile)
      onTranscriptionComplete(result)
    } catch (error: any) {
      onError(error.response?.data?.detail || error.message || 'Failed to transcribe audio')
    } finally {
      setIsUploading(false)
    }
  }

  return (
    <div className="audio-uploader">
      <div className="upload-section">
        <input
          ref={fileInputRef}
          type="file"
          accept="audio/*"
          onChange={handleFileSelect}
          disabled={isUploading}
          className="file-input"
        />
        {selectedFile && (
          <div className="file-info">
            <p>Selected: {selectedFile.name}</p>
            <p>Size: {(selectedFile.size / 1024 / 1024).toFixed(2)} MB</p>
          </div>
        )}
      </div>
      <button
        onClick={handleUpload}
        disabled={!selectedFile || isUploading}
        className="upload-button"
      >
        {isUploading ? 'Processing...' : 'Transcribe Audio'}
      </button>
    </div>
  )
}

export default AudioUploader

