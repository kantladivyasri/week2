interface TranscriptCardProps {
  transcript: string
}

const TranscriptCard = ({ transcript }: TranscriptCardProps) => {
  return (
    <div className="transcript-card">
      <h3>Transcription</h3>
      <div className="transcript-content">
        <p>{transcript}</p>
      </div>
    </div>
  )
}

export default TranscriptCard

