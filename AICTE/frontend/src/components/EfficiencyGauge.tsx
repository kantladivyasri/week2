import { EfficiencyMetrics } from '../types/api'

interface EfficiencyGaugeProps {
  efficiency: EfficiencyMetrics
}

const EfficiencyGauge = ({ efficiency }: EfficiencyGaugeProps) => {
  const percentage = efficiency.overall_score * 100
  const statusClass = efficiency.status === 'efficient' ? 'efficient' : 'needs-improvement'

  return (
    <div className="efficiency-gauge">
      <h3>Efficiency Score</h3>
      <div className="gauge-container">
        <div className="gauge">
          <div className="gauge-value">{percentage.toFixed(1)}%</div>
          <div className={`gauge-status ${statusClass}`}>
            {efficiency.status.replace('_', ' ').toUpperCase()}
          </div>
        </div>
        <div className="metrics-details">
          <div className="metric">
            <span className="metric-label">Intent Score:</span>
            <span className="metric-value">{(efficiency.intent_score * 100).toFixed(1)}%</span>
          </div>
          <div className="metric">
            <span className="metric-label">Clarity Score:</span>
            <span className="metric-value">{(efficiency.clarity_score * 100).toFixed(1)}%</span>
          </div>
          <div className="metric">
            <span className="metric-label">Urgency Score:</span>
            <span className="metric-value">{(efficiency.urgency_score * 100).toFixed(1)}%</span>
          </div>
          <div className="metric">
            <span className="metric-label">Word Count:</span>
            <span className="metric-value">{efficiency.word_count}</span>
          </div>
        </div>
      </div>
    </div>
  )
}

export default EfficiencyGauge

