import { useState, useEffect } from 'react'
import { healthCheck } from '../api/client'

interface ConnectionStatusProps {
  className?: string
}

const ConnectionStatus = ({ className }: ConnectionStatusProps) => {
  const [isConnected, setIsConnected] = useState<boolean | null>(null)
  const [isChecking, setIsChecking] = useState(true)

  useEffect(() => {
    const checkConnection = async () => {
      setIsChecking(true)
      try {
        const result = await healthCheck()
        setIsConnected(result.status === 'healthy')
      } catch (error) {
        setIsConnected(false)
      } finally {
        setIsChecking(false)
      }
    }

    checkConnection()
    // Check connection every 10 seconds
    const interval = setInterval(checkConnection, 10000)

    return () => clearInterval(interval)
  }, [])

  if (isChecking && isConnected === null) {
    return (
      <div className={`connection-status checking ${className || ''}`}>
        <span className="status-indicator checking"></span>
        <span>Checking backend connection...</span>
      </div>
    )
  }

  return (
    <div className={`connection-status ${isConnected ? 'connected' : 'disconnected'} ${className || ''}`}>
      <span className={`status-indicator ${isConnected ? 'connected' : 'disconnected'}`}></span>
      <span>
        {isConnected 
          ? 'Backend connected' 
          : 'Backend disconnected - Please ensure the backend server is running on http://localhost:8000'}
      </span>
    </div>
  )
}

export default ConnectionStatus

