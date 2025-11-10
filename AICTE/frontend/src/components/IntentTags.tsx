import { IntentScores } from '../types/api'

interface IntentTagsProps {
  intents: IntentScores
}

const IntentTags = ({ intents }: IntentTagsProps) => {
  const sortedIntents = Object.entries(intents.intents)
    .sort(([, a], [, b]) => b - a)

  return (
    <div className="intent-tags">
      <h3>Detected Intents</h3>
      <div className="top-intent">
        <span className="label">Primary Intent:</span>
        <span className="tag primary">{intents.top_intent}</span>
      </div>
      <div className="intent-list">
        {sortedIntents.map(([intent, score]) => (
          <div key={intent} className="intent-item">
            <span className="intent-name">{intent}</span>
            <div className="score-bar">
              <div
                className="score-fill"
                style={{ width: `${score * 100}%` }}
              />
            </div>
            <span className="score-value">{(score * 100).toFixed(1)}%</span>
          </div>
        ))}
      </div>
    </div>
  )
}

export default IntentTags

