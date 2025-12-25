import { useState } from 'react';

interface VideoPlayerProps {
  youtubeId: string;
  title?: string;
  onClose?: () => void;
}

export default function VideoPlayer({ youtubeId, title }: VideoPlayerProps) {
  const [isLoading, setIsLoading] = useState(true);

  return (
    <div className="w-full">
      {/* Video container with aspect ratio */}
      <div className="relative w-full aspect-video bg-gray-900 rounded-lg overflow-hidden">
        {/* Loading skeleton */}
        {isLoading && (
          <div className="absolute inset-0 flex items-center justify-center bg-gray-900">
            <div className="flex flex-col items-center gap-3">
              <div className="w-12 h-12 border-4 border-primary border-t-transparent rounded-full animate-spin" />
              <span className="text-sm text-gray-400">Loading video...</span>
            </div>
          </div>
        )}

        {/* YouTube embed */}
        <iframe
          src={`https://www.youtube.com/embed/${youtubeId}?rel=0&modestbranding=1`}
          title={title || 'Khan Academy Video'}
          allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
          allowFullScreen
          className="absolute inset-0 w-full h-full"
          onLoad={() => setIsLoading(false)}
        />
      </div>

      {/* Attribution notice */}
      <p className="text-xs text-gray-500 mt-2 text-center">
        Video from Khan Academy. Free lessons available at{' '}
        <a
          href="https://www.khanacademy.org"
          target="_blank"
          rel="noopener noreferrer"
          className="text-primary hover:underline"
        >
          khanacademy.org
        </a>
      </p>
    </div>
  );
}

// Modal version for full-screen video viewing
interface VideoModalProps {
  youtubeId: string;
  title: string;
  skillName?: string;
  onClose: () => void;
}

export function VideoModal({ youtubeId, title, skillName, onClose }: VideoModalProps) {
  return (
    <div className="fixed inset-0 bg-black bg-opacity-95 flex items-center justify-center p-2 sm:p-4 z-50 safe-area-inset">
      <div className="w-full max-w-4xl">
        {/* Header */}
        <div className="flex items-center justify-between mb-4">
          <div>
            <h2 className="text-xl sm:text-2xl font-bold text-white">{title}</h2>
            {skillName && (
              <p className="text-sm text-gray-400">{skillName}</p>
            )}
          </div>
          <button
            onClick={onClose}
            className="p-2 text-gray-400 hover:text-white transition-colors"
            aria-label="Close video"
          >
            <svg className="w-6 h-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M6 18L18 6M6 6l12 12" />
            </svg>
          </button>
        </div>

        {/* Video player */}
        <VideoPlayer youtubeId={youtubeId} title={title} />

        {/* Close button */}
        <div className="mt-4 flex justify-center">
          <button
            onClick={onClose}
            className="btn-secondary px-6"
          >
            Close Video
          </button>
        </div>
      </div>
    </div>
  );
}

// Compact video card for lists
interface VideoCardProps {
  youtubeId: string;
  title: string;
  skillName: string;
  onClick: () => void;
}

export function VideoCard({ youtubeId, title, skillName, onClick }: VideoCardProps) {
  return (
    <button
      onClick={onClick}
      className="w-full text-left bg-surface border border-gray-800 rounded-lg p-3 hover:border-primary transition-all group"
    >
      <div className="flex items-center gap-3">
        {/* Thumbnail placeholder with play button */}
        <div className="relative w-20 h-12 bg-gray-800 rounded overflow-hidden flex-shrink-0">
          <img
            src={`https://img.youtube.com/vi/${youtubeId}/mqdefault.jpg`}
            alt={title}
            className="w-full h-full object-cover"
          />
          <div className="absolute inset-0 flex items-center justify-center bg-black bg-opacity-40 group-hover:bg-opacity-20 transition-all">
            <div className="w-8 h-8 rounded-full bg-primary flex items-center justify-center">
              <svg className="w-4 h-4 text-white ml-0.5" fill="currentColor" viewBox="0 0 24 24">
                <path d="M8 5v14l11-7z" />
              </svg>
            </div>
          </div>
        </div>

        {/* Info */}
        <div className="flex-1 min-w-0">
          <p className="text-sm font-medium text-white truncate">{title}</p>
          <p className="text-xs text-gray-500 truncate">{skillName}</p>
        </div>

        {/* Arrow */}
        <svg className="w-5 h-5 text-gray-600 group-hover:text-primary transition-colors" fill="none" viewBox="0 0 24 24" stroke="currentColor">
          <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 5l7 7-7 7" />
        </svg>
      </div>
    </button>
  );
}
