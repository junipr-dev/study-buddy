import { api } from './client';
import type { Badge } from '../types';

/**
 * Get all badges with earned status for current user.
 */
export async function getAllBadges(): Promise<Badge[]> {
  return api.get<Badge[]>('/badges');
}

/**
 * Get only earned badges for current user.
 */
export async function getEarnedBadges(): Promise<Badge[]> {
  return api.get<Badge[]>('/badges/earned');
}
